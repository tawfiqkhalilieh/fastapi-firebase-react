import { MutableRefObject, useRef, useState } from "react";
import LoginHandler from "../../utils/login";
import { Fade } from "react-awesome-reveal";
import setCookies from "../../utils/cookies/set_cookies";
import get_cookies from "../../utils/cookies/get_cookies";

const Login = () => {
  if (get_cookies("id")) {
    window.location.href = "/dashboard";
  }
  // login refs
  const [acativity, setAcativity] = useState(true);
  const btn: MutableRefObject<null> = useRef(null);
  const email: MutableRefObject<null> = useRef(null);
  const password: MutableRefObject<null> = useRef(null);

  // signup refs
  const username: MutableRefObject<null> = useRef(null);
  const age: MutableRefObject<null> = useRef(null);
  const birthday: MutableRefObject<null> = useRef(null);
  const gender: MutableRefObject<null> = useRef(null);

  const submitHandler = async () => {
    // @ts-ignore
    const username_value = username.current ? username.current.value : null;
    if (username_value === null) {
      // @ts-ignore
      const email_value = email.current.value;
      // @ts-ignore
      const password_value = password.current.value;
      const res = await LoginHandler(email_value, password_value);
      if (res)
        // @ts-ignore
        for (let key of Object.keys(res)) {
          await setCookies(key, res[key]);
          window.location.href = "/dashboard";
        }
      else {
        return;
      }
    }
  };

  return acativity ? (
    <div className="loginContainer">
      <Fade>
        <div className="login-box">
          <h2>Login</h2>
          <form>
            <div className="user-box">
              <input
                type="text"
                id="email"
                autoComplete="off"
                ref={email}
                required
              />
              <label>email</label>
            </div>
            <div className="user-box">
              <input
                type="password"
                id="password"
                autoComplete="off"
                ref={password}
                required
              />
              <label>password</label>
            </div>
            <div className="buttons">
              <a
                id="btn"
                ref={btn}
                onMouseOver={() => {
                  if (
                    // @ts-ignore
                    document.getElementById("email").value === "" ||
                    // @ts-ignore
                    document.getElementById("password").value === ""
                  ) {
                    // @ts-ignore
                    btn.current.classList.contains("a")
                      ? // @ts-ignore
                        btn.current.classList.remove("a")
                      : // @ts-ignore
                        btn.current.classList.add("a");
                  }
                }}
                onClick={() =>
                  // @ts-ignore
                  {
                    if (
                      // @ts-ignore
                      document.getElementById("email").value === "" ||
                      // @ts-ignore
                      document.getElementById("password").value === ""
                    ) {
                      // @ts-ignore
                      return btn.current.classList.contains("a")
                        ? // @ts-ignore
                          btn.current.classList.remove("a")
                        : // @ts-ignore
                          btn.current.classList.add("a");
                    } else {
                      submitHandler();
                    }
                  }
                }
              >
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Login
              </a>
            </div>
          </form>
        </div>
        <h3
          className="paragraph"
          onClick={() => {
            [
              // @ts-ignore
              email.current.value,
              // @ts-ignore
              password.current.value,
            ] = ["", "", "", "", "", ""];
            setAcativity(false);
          }}
        >
          Click here to signup
        </h3>
      </Fade>
    </div>
  ) : (
    <Fade>
      <div className="loginContainer">
        <div className="login-box">
          <h2>Signup</h2>
          <form>
            <div className="user-box">
              <input
                type="text"
                id="email"
                autoComplete="off"
                ref={email}
                required
              />
              <label>email</label>
            </div>
            <div className="user-box">
              <input
                type="text"
                id="username"
                autoComplete="off"
                ref={username}
                required
              />
              <label>username</label>
            </div>
            <div className="user-box">
              <input
                type="password"
                id="password"
                autoComplete="off"
                ref={password}
                required
              />
              <label>password</label>
            </div>
            <div className="user-box">
              <input
                type="number"
                id="age"
                autoComplete="off"
                ref={age}
                required
              />
              <label>age</label>
            </div>
            <div className="user-box">
              <input
                type="date"
                id="birthday"
                autoComplete="on"
                ref={birthday}
                value={"2023-01-01"}
                data-date-format="DD MMMM YYYY"
                required
              />
              <label>birthday</label>
            </div>
            <div className="user-box">
              <input
                type="text"
                id="gender"
                autoComplete="on"
                ref={gender}
                required
              />
              <label>gender</label>
            </div>
            <div className="buttons">
              <a
                id="btn"
                ref={btn}
                onMouseOver={() => {
                  if (
                    // @ts-ignore
                    document.getElementById("email").value === "" ||
                    // @ts-ignore
                    document.getElementById("password").value === ""
                  ) {
                    // @ts-ignore
                    btn.current.classList.contains("a")
                      ? // @ts-ignore
                        btn.current.classList.remove("a")
                      : // @ts-ignore
                        btn.current.classList.add("a");
                  }
                }}
                onClick={() =>
                  // @ts-ignore
                  {
                    if (
                      // @ts-ignore
                      document.getElementById("email").value === "" ||
                      // @ts-ignore
                      document.getElementById("password").value === ""
                    ) {
                      // @ts-ignore
                      return btn.classList.contains("a")
                        ? // @ts-ignore
                          btn.current.classList.remove("a")
                        : // @ts-ignore
                          btn.current.classList.add("a");
                    }
                    // alert("Logged in successfuly");
                    // // @ts-ignore
                    submitHandler();
                  }
                }
              >
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Sigunup
              </a>
            </div>
          </form>
        </div>
        <h3
          className="paragraph2"
          onClick={() => {
            [
              // @ts-ignore
              email.current.value,
              // @ts-ignore
              password.current.value,
              // @ts-ignore
              username.current.value,
              // @ts-ignore
              age.current.value,
              // @ts-ignore
              birthday.current.value,
              // @ts-ignore
              gender.current.value,
            ] = ["", "", "", "", "", ""];
            setAcativity(true);
          }}
        >
          Click here to login
        </h3>
      </div>
    </Fade>
  );
};

export default Login;
