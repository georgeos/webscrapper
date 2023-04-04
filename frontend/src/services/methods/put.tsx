import { handleResponse } from "../handleResponse";

export const put = async (url: string, body: string, contentType: string = 'application/json') => {
  return await fetch(url,
    {
      method: 'PUT',
      headers: { 'Content-Type': contentType },
      body: body
    })
    .then((response) => {
      return handleResponse(response);
    })
}