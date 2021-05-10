import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import Popup from 'reactjs-popup';
import './UserMenu.css'

const UserMenu = () => {

  const [displayCreate, setDisplayCreate] = useState('false')
  const [name, setName] = useState('')
  const [tag, setTag] = useState('')
  const [description, setDescription]= useState('')
  const tagId = '';

  const handleCreate = (e) => {
    e.preventDefault()
    let newCreature= {
      name,

    }
  }
  return (
    <div className='usermenu__container'>
      <div className='usermenu__option'>
        <div className='usermenu__option' onClick={() => setDisplayCreate(true)}>Create Custom</div>
        <Popup open={displayCreate} onClose={()=> setDisplayCreate(false)}>
          <form className='create__form' onSubmit={handleCreate}>
            <div>
              <label name='name'>Creature Name: </label>
              <input
              type='text'
              onChange={(e)=> setName(e.target.value)}></input>
            </div>

            <div>
              <label name='tag'>Select a Tag:</label>
              <select name='tag'>
                <option value='Lore' onChange={(e)=> setTag(e.target.value)}>Lore</option>
                <option value='Custom' onChange={(e)=> setTag(e.target.value)}>Custom</option>
              </select>
            </div>

            <div>
              <label name ='description'>Creature Description:</label>
              <textarea type='textarea'
              onChange={(e) => setDescription(e.target.value)}></textarea>
            </div>

            <button>Create New Creature</button>
          </form>
        </Popup>
      </div>
      <div className='usermenu__option'>
        <LogoutButton />
      </div>
    </div>
  )
}

export default UserMenu
