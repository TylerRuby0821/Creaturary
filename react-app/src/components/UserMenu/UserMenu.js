import React, { useState } from 'react';
import {useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import Popup from 'reactjs-popup';
import './UserMenu.css'
import { useDispatch, useSelector } from 'react-redux';
import {createCreature} from '../../store/creature'

const UserMenu = () => {
  const allTags = useSelector(state => state.tag)
  const dispatch= useDispatch()
  const history = useHistory()
  const [displayCreate, setDisplayCreate] = useState(false)
  const [name, setName] = useState('')
  const [tag, setTag] = useState('')
  const [description, setDescription]= useState('')

  // const lore =
  // const custom =
  // for (const tagg in allTags) {
    // console.log("CREAT", allCreatures[creat].id)
  //   if (allTags[tagg].type === tag){
  //     tags = {...allTags[tagg]}

  //   }
  // }
  // const tagId = tags.id;
  // console.log('TAGID', tagId)


  const handleCreate = async (e) => {
    e.preventDefault()
    let newCreature= {
      name,
      tag,
      description
    }
    const creature = await dispatch(createCreature(newCreature))
    // console.log('CREATURE ------->', creature)
    history.push(`/creatures/${creature.id}`)
  }

  return (
    <div className='usermenu__container'>
      <div className='usermenu__option'>
        <div className='usermenu__option' onClick={() => setDisplayCreate(true)}>Create Custom</div>
        <Popup open={displayCreate} onClose={()=> setDisplayCreate(false)}>
          <form className='create__form' onSubmit={handleCreate}>
            <div className='form__item'>
              <label name='name' className='form__label'>Creature Name: </label>
              <input
              type='text'
              onChange={(e)=> setName(e.target.value)}></input>
            </div>

            <div className='form__item'>
              <label name='tag' className='form__label'>Select a Tag:</label>
              <select name='tag' value={tag} onChange={(e) => {setTag(e.target.value)}}>
                <option defaultValue value='' disabled>Select a Tag</option>
                {Object.values(allTags).map(tag => {
                  return <option key={tag.id} value ={tag.id}> {tag.type}</option>
                })}
              </select>
            </div>

            <div className='form__item'>
              <label name ='description' className='form__label'>Creature Description:</label>
              <textarea type='textarea'
              className='description'
              onChange={(e) => setDescription(e.target.value)}></textarea>
            </div>

            <button className='submit__create'>Create New Creature</button>
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
