import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";
import { useHistory, Redirect } from 'react-router-dom'
import './LogoutButton.css'

const LogoutButton = () => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogout = async (e) => {
    await dispatch(logout(user));
    // Redirect('/')
  };

  return <div className='logout__button' onClick={onLogout}>Logout</div>;
};

export default LogoutButton;
