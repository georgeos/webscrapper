import { IconButton, Stack, Typography } from '@mui/material';
import Box from '@mui/material/Box';
import NavigateNextIcon from '@mui/icons-material/NavigateNext';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';

const Table = (props: { time?: number, header: any, body: any, children?: any, onPrevious: any, onNext: any, previous: string, next: string, current: string }) => {

  const res = props.current ? props.current.match(/\d+$/) : '1';
  const pageNumber = res && res[0] ? res[0] : '1';
  const handlePrevious = () => props.onPrevious();
  const handleNext = () => props.onNext();

  return (
    <Box sx={{ height: 'auto', width: 'auto' }} flexDirection="column" justifyContent="center" alignItems="center">
      <Stack direction="row" justifyContent="flex-end" alignItems="center">
        <IconButton disabled={!props.previous} onClick={handlePrevious}><NavigateBeforeIcon></NavigateBeforeIcon></IconButton>
        <Typography>{pageNumber}</Typography>
        <IconButton disabled={!props.next} onClick={handleNext}><NavigateNextIcon></NavigateNextIcon></IconButton>
      </Stack>
      <table style={{ border: '2px solid #555' }}>
        {props.header}
        {props.body}
      </table>
    </Box>
  );
}

export default Table;