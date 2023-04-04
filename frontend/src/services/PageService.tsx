import { get } from "./methods/get";
import { post } from "./methods/post";

export const API_URL = process.env.NEXT_PUBLIC_API;

const GetPages = async (url?: string) => {
  url = url ?? `${API_URL}/pages/?page=1`;
  return await get(url);
};

const GetLinks = async (pageId: number, url?: string) => {
  url = url ?? `${API_URL}/pages/${pageId}/links?page=1`;
  return await get(url);
};

const ScrapePage = async (body: any) => {
  const json = JSON.stringify(body);
  return await post(`${API_URL}/pages/`, json);
};

export { GetPages, ScrapePage, GetLinks }