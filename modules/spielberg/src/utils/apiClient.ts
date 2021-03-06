import axios from "axios";
import { KUBRICK_URL } from "./constants";

export const kubrick = axios.create({
  baseURL: KUBRICK_URL,
  headers: {
    "Content-Type": "application/json;charset=UTF-8",
  },
});
