import { GetPages } from '@/services/PageService';
import { Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import { Page } from '../models/Page';
import Table from './Table';

const PagesTable = (props: { time: number }) => {

  const [pages, setPages] = useState<Page[]>([]);
  const [previous, setPrevious] = useState<string>('');
  const [next, setNext] = useState<string>('');
  const [url, setUrl] = useState<string>();
  const router = useRouter();
  const columns = [
    { field: 'name', headerName: 'Name', width: 300 },
    { field: 'num_links', headerName: 'Total links', width: 90 },
  ];

  const handlePrevious = () => setUrl(previous);
  const handleNext = () => setUrl(next);
  const handleNavigation = (pageId: number, pageName: string) => { router.push(`/page/${pageId}?name=${pageName}`, `/page/${pageId}`) }

  useEffect(() => {

    const fetchData = async () => {
      GetPages(url)
        .then((response) => {
          setPages(response.results);
          setPrevious(response.previous);
          setNext(response.next);

          const processing: Page[] = response.results.filter((p: Page) => p.status == 'Processing');
          if (processing && processing.length == 0) {
            clearInterval(interval);
          }
        })
        .catch(() => { });
    }

    fetchData();

    const interval = setInterval(() => {
      fetchData();
    }, 2000);

    return () => clearInterval(interval);

  }, [props.time, url])

  return (
    <Table
      previous={previous}
      next={next}
      onPrevious={handlePrevious}
      onNext={handleNext}
      current={url!}
      time={props.time}
      header={
        <thead>
          <tr style={{ border: '2px solid #555' }}>
            {
              columns.map(c => (
                <th style={{ width: c.field == 'name' ? 500 : 100 }} ><Typography>{c.headerName}</Typography></th>
              ))
            }
          </tr>
        </thead>}
      body={<tbody>
        {
          pages.map(p => (
            <tr>
              {
                columns.map(c => (
                  <td style={{ border: '1px solid #eee', cursor: 'pointer' }} onClick={() => handleNavigation(p.id, p.name)}>
                    <Typography>
                      {
                        c.field == 'name'
                          ? p.name
                          : p.num_links == 0
                            ? p.status
                            : p.num_links
                      }
                    </Typography>
                  </td>
                ))

              }
            </tr>
          ))
        }
      </tbody>}>
    </Table>
  );
}

export default PagesTable;