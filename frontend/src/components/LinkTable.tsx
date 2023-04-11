import { Link } from '@/models/Link';
import { GetLinks } from '@/services/PageService';
import { IconButton, Stack, Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';
import Table from './Table';

const LinkTable = () => {

  const [links, setLinks] = useState<Link[]>([]);
  const [previous, setPrevious] = useState<string>('');
  const [next, setNext] = useState<string>('');
  const [url, setUrl] = useState<string>();
  const router = useRouter();
  const pageName = router.isReady ? router.query.name : '';
  const columns = [
    { field: 'name', headerName: 'Name', width: 300 },
    { field: 'url', headerName: 'Link', width: 90 },
  ];

  const handlePrevious = () => setUrl(previous);
  const handleNext = () => setUrl(next);
  const handleBack = () => router.push(`/`);

  useEffect(() => {

    const fetchData = async () => {
      if (router.isReady) {
        const pageId = router.query.pageId as string;
        GetLinks(+pageId, url)
          .then((response) => {
            setLinks(response.results);
            setPrevious(response.previous);
            setNext(response.next);
          })
          .catch(() => { });
      }
    }

    fetchData();
  }, [url])

  return (
    <Stack direction="column" spacing={1} justifyContent="center" alignItems="center">
      <Typography variant="h5">
        <IconButton onClick={handleBack}>
          <NavigateBeforeIcon></NavigateBeforeIcon>
        </IconButton>{pageName}
      </Typography>
      <Table
        previous={previous}
        next={next}
        onPrevious={handlePrevious}
        onNext={handleNext}
        current={url!}
        header={<thead>
          <tr style={{ border: '2px solid #555' }}>
            {
              columns.map(c => (
                <th key={c.field} style={{ width: c.field == 'name' ? 200 : 400 }} ><Typography>{c.headerName}</Typography></th>
              ))
            }
          </tr>
        </thead>}
        body={<tbody>
          {
            links.map(l => (
              <tr key={l.id}>
                {
                  columns.map(c => (
                    <td key={c.field} style={{ border: '1px solid #eee', width: c.field == 'name' ? 200 : 400, textOverflow: 'ellipsis', overflow: "hidden" }}>
                      <Typography noWrap textOverflow="ellipsis">
                        {
                          c.field == 'name'
                            ? l.name
                            : l.url
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
    </Stack>
  );
}

export default LinkTable;