import React from 'react';
import './Footer.css'

const Footer = () => {
  return (
    <div className='footer__container'>
      <a className='footer__link' href='https://github.com/TylerRuby0821'>
        <img className='footer__image' src= '/GitHub-Mark.png' alt='GitHub' height={50} width={50}></img>
      </a>
      <a className='footer__link' href='https://www.linkedin.com/in/tyler-ruby-b700161ba/'>
        <img className='footer__image' src= '/LI-In-Bug.png' alt='LinkedIn' height={50} width={50}></img>
      </a>
      {/* <a className='footer__link' href=''> */}
        {/* <img className='footer__link' src='' alt='' height={50} width={50}></img> */}
      {/* </a> */}
    </div>
  )
}


export default Footer
