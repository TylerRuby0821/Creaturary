import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";
import { useHistory } from 'react-router-dom'

const LogoutButton = ({setAuthenticated}) => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogout = async (e) => {
    await dispatch(logout(user));
    history.push('/')
  };

  return <button onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
