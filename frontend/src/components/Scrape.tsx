import { ScrapePage } from "@/services/PageService";
import { Button, Stack, TextField, Snackbar, Alert } from "@mui/material";
import { useState } from "react";
import PagesTable from "./PageTable";

const Scrape = () => {

  const [page, setPage] = useState<string>();
  const [time, setTime] = useState<number>(0);
  const [displayError, setDisplayError] = useState<boolean>();

  const handleScrape = () => {
    const body = { url: page };
    ScrapePage(body)
      .then(() => {
        setTime(new Date().getTime())
        setPage('');
      })
      .catch(() => {
        setDisplayError(true);
      })
  }

  return (
    <Stack direction="column" width="100vw" height="100vh" spacing={2} justifyContent="center" alignItems="center">
      <Stack direction="row" width="100vw" spacing={2} justifyContent="center" alignItems="center">
        <TextField variant="outlined" value={page} label="New page" onChange={(e) => setPage(e.target.value)}></TextField>
        <Button variant="contained" color="primary" onClick={handleScrape} disabled={!page}>Scrape</Button>
      </Stack>
      <PagesTable time={time}></PagesTable>
      <Snackbar open={displayError} autoHideDuration={3000} anchorOrigin={{ horizontal: 'right', vertical: 'top' }}>
        <Alert onClose={() => setDisplayError(false)} severity="error">
          Error in the url provided
        </Alert>
      </Snackbar>
    </Stack>
  )
}

export default Scrape;