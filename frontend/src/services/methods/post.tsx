import { HttpError } from "@/models/HttpError";
import { handleResponse } from "../handleResponse";

export const post = async (url: string, body: string, contentType: string = 'application/json') => {
  return await fetch(url,
    {
      method: 'POST',
      headers: { 'Content-Type': contentType },
      body: body
    })
    .then((response) => {
      return handleResponse(response);
    })
    .catch((e) => {
      throw new Error("Error while retrieving data");
    })
}
