import React from "react";
import { useDispatch} from "react-redux";
import { logout } from "../../store/session";

import './LogoutButton.css'

const LogoutButton = () => {
  const dispatch = useDispatch();

  const onLogout = () => {
   dispatch(logout());
  };

  return <div className='logout__button' onClick={onLogout}>Logout</div>;
};

export default LogoutButton;
