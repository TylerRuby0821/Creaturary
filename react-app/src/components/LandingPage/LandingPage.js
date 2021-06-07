import React from 'react';
import { Redirect, NavLink } from 'react-router-dom';
import { useSelector } from "react-redux";
import './LandingPage.css'
import Footer from '../Footer/Footer'
const LandingPage = () => {
  const user = useSelector(state => state.session.user);

  if (user) {
    return <Redirect to="/creatures" />;
  }

  return (
    <div className='landing__container'>
      <h1 className='landing__header'>Creaturary</h1>
      <h3 className='landing__subheader'>All things spooky, mythical, magical and beyond...</h3>
      <div className='landing__nav--container'>
        <NavLink className='landing__login--nav' to='/login'> Login </NavLink>
        <NavLink className='landing__signup--nav' to='/sign-up'> Signup </NavLink>
      </div>
      <Footer />
    </div>
  )
}

export default LandingPage
