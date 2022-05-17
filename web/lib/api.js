import axios from 'axios';
axios.defaults.withCredentials = true
axios.defaults.baseURL = `${process.env.NEXT_PUBLIC_API_HOST}/api`;
axios.defaults.headers.common['Content-Type'] = 'application/json'

export const axiosApi = axios;

export const login = async (data) => {
  const response  = await axiosApi.post("/token", data);
  return response.data;
};

export const getUsages = async (...args) => {
  const [api, page] = args;
  const response = await api.get(`/usages?page=${page}`);
  return response.data;
}