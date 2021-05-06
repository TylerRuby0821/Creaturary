import React, {useState} from 'react';
import './Navigation.css'
import { useSelector } from 'react-redux'
import UserMenu from '../UserMenu/UserMenu'

const Navigation = () => {

  const user = useSelector(state => state.session.user)
  const [menu, setMenu] = useState(false)

  const handleMenu = () => {
    setMenu(true)

  }

  return (
    <div className='navbar__container'>
      <div className='navbar__header--container'>
        <h1 className='navbar__header'>Creaturary</h1>
      </div>
      <div className='navbar__search--container'>
        {/* Search Bar Here */}
      </div>
      <div className='navbar__user--container'>
        <h3 className='navbar__username'>{user.username}</h3>
        <span className='navbar__usermenu'>
          <i class="fas fa-bars"  onClick={() => setMenu(!menu)}></i>
        </span>
        {menu &&
          <div className='usermenu'>
            <UserMenu />
          </div>
        }
      </div>
    </div>

  );
}

export default Navigation;
