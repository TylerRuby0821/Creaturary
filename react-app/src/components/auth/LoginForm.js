import React, { useState } from "react";
import { Redirect, NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {login } from "../../store/session";
import './LoginForm.css'
import {getFavorites} from '../../store/favorite'

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user)
  const sessionLoaded = useSelector(state => state.session.loaded)
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = (e) => {
    e.preventDefault();
    dispatch(login(email, password))
      .catch(err => setErrors(err.errors))
  };

  const handleDemo = (e) => {
    e.preventDefault();
    dispatch(login('demo@aa.io','password'))
      .catch(err => setErrors(err.errors))
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (sessionLoaded && user) {
    dispatch(getFavorites())
    return <Redirect to="/creatures" />;
  }

  return (
    <div className='login__container'>
      <div className='login__header'><NavLink className='login__header' to='/'>Creaturary</NavLink></div>
      <form className='login__form' onSubmit={onLogin}>
        <div>
          {errors.map((error) => (
            <div key={error} className='error__message'>{error}</div>
          ))}
        </div>
        <div>
          {/* <label htmlFor="email">Email</label> */}
          <input
            className='login__form--input'
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          {/* <label htmlFor="password">Password</label> */}
          <input
            className='login__form--input pass'
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
          />
          <div className='login__form--buttons'>
            <button className='login__form--button' type="submit">Login</button>
            <button className='login__form--button' type='submit' onClick={handleDemo}>Demo</button>
          </div>
        </div>
        <div className='login__form--nav'> Dont have an account? <NavLink className='login__nav--button' to='/sign-up'>Sign Up Here</NavLink></div>
      </form>
    </div>
  );
};

export default LoginForm;
