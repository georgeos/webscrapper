import { handleResponse } from "../handleResponse";

export const get = async (url: string) => {
  return await fetch(url,
    {
      method: 'GET'
    })
    .then((response) => {
      return handleResponse(response);
    })
}