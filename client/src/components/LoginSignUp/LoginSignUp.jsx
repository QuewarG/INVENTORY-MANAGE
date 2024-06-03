import React from "react";

//import "../../components/LoginSignUp/LoginSignUp.scss";
import { FaLock, FaUser } from "react-icons/fa";
import { Link } from "react-router-dom";

const LoginSignUp = () => {
  return (
    <div className="login-container">
        <form action="">
            <h1> Login </h1>
            <div className="input-box">
                <input type="text" placeholder="Username" required/>
                <i><FaUser/></i>
            </div>
            <div className="input-box">
                <input type="password" placeholder="Password" required/>
                <i><FaLock/></i>
            </div>
            <div className="remember-forgot">
                <label><input type="checkbox"/> Remember me </label>
                <a href="#"> Forgot Password </a>
            </div>

            <Link to="/"> <button type="submit" className="btn"> Login </button> </Link>

            <div className="register-link">
                <p>Don't have an account? <a href="#">
                    Register</a></p>
            </div>
        </form>

    </div>
  )
}

export default LoginSignUp;