import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";
import { useHistory, Redirect } from 'react-router-dom'
import './LogoutButton.css'

const LogoutButton = () => {
  const dispatch = useDispatch();

  const onLogout = () => {
   dispatch(logout());
  };

  return <div className='logout__button' onClick={onLogout}>Logout</div>;
};

export default LogoutButton;
