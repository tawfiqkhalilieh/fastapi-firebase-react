import axios from "axios";

const LoginHandler = async (email: string, password: string) => {
  let response;
  // example:
  // email = "me@tawfiq.dev";
  // password = "hkkrne";
  try {
    await axios
      .get(`http://localhost:8000/login/${email}/${password}`)
      .then((res) => {
        console.log(res.data);
        response = { ...res.data };
      });
  } catch (err) {
    console.warn(err);
  }
  console.log(response);
  // @ts-ignore
  return response;
};

export default LoginHandler;
