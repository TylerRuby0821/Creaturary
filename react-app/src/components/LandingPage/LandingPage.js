import React from 'react';
import { NavLink } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div className='landing__container'>
      <h1 className='landing__header'>Creaturary</h1>
      <h3>All things spooky, mythical, magical and beyond!</h3>
      <NavLink to='/login'> Login </NavLink>
      <NavLink to='/sign-up'> Signup </NavLink>
    </div>
  )
}

export default LandingPage
