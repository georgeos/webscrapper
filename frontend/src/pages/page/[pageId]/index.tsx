import LinkTable from "@/components/LinkTable";
import Stack from "@mui/material/Stack";

export default function Home() {
  return (
    <Stack direction="column" width="100vw" height="100vh" spacing={2} justifyContent="center" alignItems="center">
      <LinkTable></LinkTable>
    </Stack>
  )
}
