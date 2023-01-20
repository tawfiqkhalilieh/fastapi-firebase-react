import Cookies from "universal-cookie";

const get_cookies = (key: string) => {
  const cookies = new Cookies();
  return cookies.get(key);
};
export default get_cookies;
