import React from 'react';
import './Footer.css'
import github from './GitHub-Mark.png'
import linkedIn from './LI-In-Bug.png'

const Footer = () => {
  return (
    <div className='footer__container'>
      <div className='footer__header'>
        <div className= 'footer__header--text'>
          <h1>Created By:</h1>
          <h1>Tyler Ruby</h1>
        </div>
        <a className='footer__link' href='https://github.com/TylerRuby0821'>
          <img className='footer__image' src= {github} alt='GitHub' height={50} width={50}></img>
        </a>
        <a className='footer__link' href='https://www.linkedin.com/in/tyler-ruby-b700161ba/'>
          <img className='footer__image' src= {linkedIn} alt='LinkedIn' height={50} width={50}></img>
        </a>
        <a className='footer__link' href='https://tylerruby0821.github.io/'>
          <div className='portfolio'>P</div>
        </a>
      </div>
    </div>
  )
}


export default Footer
