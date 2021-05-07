import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './UserMenu.css'

const UserMenu = () => {
  return (
    <div className='usermenu__container'>
      <div className='usermenu__option'>
        <NavLink className='usermenu__option' to ='/creatures/create'>Create Custom</NavLink>
      </div>
      <div className='usermenu__option'>
        <LogoutButton />
      </div>
    </div>
  )
}

export default UserMenu
