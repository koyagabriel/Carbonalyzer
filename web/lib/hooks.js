import { useContext } from "react";
import { AuthContext } from "./context";
import { axiosApi } from "./api";

export const useAuth = () => useContext(AuthContext);

export const useAxiosApi = () => {
  const { auth } = useAuth();
  axiosApi.defaults.headers.common['Authorization'] = `Bearer ${auth?.access}`;
  return axiosApi;
};