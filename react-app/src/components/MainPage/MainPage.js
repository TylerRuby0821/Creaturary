import React from 'react';
import { NavLink, Redirect} from 'react-router-dom';
import { useSelector} from 'react-redux'
import Navigation from '../Naviagtion/Navigation'
import './MainPage.css'



const MainPage = () => {

  const user = useSelector(state => state.session.user)


  // const handleSubmit = (e) => {
  //   e.preventDefault()
  //   // dispatch(getCreaturesSearch(search))
  //   history.push({
  //     pathname: '/creatures/search',
  //     search: search
  //   })
  // }

  return (
    <div>
      {/* {(user) ? */}
        <div className='main__container'>
          <Navigation />
          {/* <div className='positional__helper'> */}
            <div className='main__search--container'>
              <p className='main__search--header'>Peak behind the curtain...</p>

            </div>
          {/* </div> */}
          <div className='main__body'>
            <div className='main__body--lore'>
              <NavLink to='/creatures/lore'>
                <i className="fas fa-book"></i>
                <div className='book__text'>Lore</div>
              </NavLink>
            </div>
            <div className='main__body--az'>
              <NavLink to='/creatures/a-z'>
                <i className="fas fa-book"></i>
                <div className='book__text'>A-Z</div>
              </NavLink>
            </div>
            <div className='main__body--custom'>
              <NavLink to='/creatures/custom'>
                <i className ="fas fa-book"></i>
                <div className='book__text'>Custom</div>
              </NavLink>
            </div>
          </div>
          <div className='favorites__header'> My Favorites: </div>
        </div>
        {/* : Redirect('/')} */}
    </div>
  )
}

export default MainPage
