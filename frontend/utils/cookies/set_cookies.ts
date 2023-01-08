import Cookies from "universal-cookie";

const setCookies = (key: string, value: string, path: string = "/") => {
  const cookies = new Cookies();
  cookies.set(key, value, { path: path });
};

export default setCookies;
