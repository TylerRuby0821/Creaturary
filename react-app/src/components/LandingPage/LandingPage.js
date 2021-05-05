import React from 'react';
import { NavLink } from 'react-router-dom';
import './LandingPage.css'

const LandingPage = () => {
  return (
    <div className='landing__container'>
      <h1 className='landing__header'>Creaturary</h1>
      <h3 className='landing__subheader'>All things spooky, mythical, magical and beyond...</h3>
      <div className='landing__nav--container'>
        <NavLink className='landing__login--nav' to='/login'> Login </NavLink>
        <NavLink className='landing__signup--nav' to='/sign-up'> Signup </NavLink>
      </div>
    </div>
  )
}

export default LandingPage
