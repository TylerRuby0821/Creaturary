import React, { useState } from "react";
import { Redirect, NavLink } from 'react-router-dom';
import { signUp } from '../../store/session';
import { useDispatch, useSelector } from "react-redux";
import './SignUpForm.css'

const SignUpForm = ({authenticated, setAuthenticated}) => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      await dispatch(signUp(username, email, password));
      if (!user.errors) {
        setAuthenticated(true);
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/creatures" />;
  }

  return (
    <div className='signup__container'>
      <div className='signup__header'><NavLink className='signup__header' to='/'>Creaturary</NavLink></div>
      <form className='signup__form' onSubmit={onSignUp}>
        <div>
          {/* <label>User Name</label> */}
          <input
            className='signup__form--input'
            placeholder='Username'
            type="text"
            name="username"
            onChange={updateUsername}
            value={username}
          ></input>
        </div>
        <div>
          {/* <label>Email</label> */}
          <input
            className='signup__form--input'
            placeholder='Email'
            type="text"
            name="email"
            onChange={updateEmail}
            value={email}
          ></input>
        </div>
        <div>
          {/* <label>Password</label> */}
          <input
            className='signup__form--input'
            placeholder='Password'
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
          ></input>
        </div>
        <div>
          {/* <label>Repeat Password</label> */}
          <input
            className='signup__form--input'
            placeholder='Confirm Password'
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div>
        <button className='signup__form--button' type="submit">Sign Up</button>
        <div className='signup__form--nav'> Already have an account? <NavLink className='signup__nav--button' to='/login'>Login Here</NavLink></div>
      </form>
    </div>
  );
};

export default SignUpForm;
