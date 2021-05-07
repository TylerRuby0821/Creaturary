import React, {useState} from 'react';
import './Navigation.css'
import { useSelector } from 'react-redux'
import UserMenu from '../UserMenu/UserMenu'
import { NavLink, Redirect } from 'react-router-dom';

const Navigation = () => {

  const user = useSelector(state => state.session.user)
  const [menu, setMenu] = useState(false)

  return (
    <div>
      {user &&
        <div className='navbar__container'>
          <div className='navbar__header--container'>
            <h1 className='navbar__header'><NavLink className='navbar__header' to='/creatures'>Creaturary</NavLink></h1>
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
      }

    </div>

  );
}

export default Navigation;
