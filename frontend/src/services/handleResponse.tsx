import { HttpError } from "../models/HttpError";

const getErrors = (json: any) => {
  if (json.errors && json.errors.GeneralErrors)
    return json.errors.GeneralErrors.join('\n');
  else if (json.errors)
    return json.errors;
}

export const handleResponse = (response: Response) => {
  if (response.ok)
    return response.json();
  else
    return response.json()
      .then(json => {
        throw new HttpError(response.status, getErrors(json));
      })
      .catch((e: Error) => {
        throw new HttpError(response.status, e.message);
      });
}

