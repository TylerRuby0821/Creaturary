import React, { useState } from 'react';
import {useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import Popup from 'reactjs-popup';
import './UserMenu.css'
import { useDispatch, useSelector } from 'react-redux';
import {createCreature} from '../../store/creature'
import S3FileUpload from 'react-s3'
import { createImage } from '../../store/image';

const UserMenu = () => {
  const allTags = useSelector(state => state.tag)
  const dispatch= useDispatch()
  const history = useHistory()
  const [displayCreate, setDisplayCreate] = useState(false)
  const [name, setName] = useState('')
  const [tag, setTag] = useState('')
  const [description, setDescription]= useState('')
  const [errors, setErrors] = useState([]);


  const config = {
    bucketName: 'creaturary',
    // dirName: '', /* optional */
    region: 'us-east-1',
    accessKeyId: process.env.REACT_APP_S3_KEY,
    secretAccessKey: process.env.REACT_APP_S3_SECRET
  }


  let url = ''
  const upload = (e) => {
      S3FileUpload.uploadFile(e.target.files[0], config)
      .then((data) => {
         url = data.location
      })
  }


  const handleCreate = async (e) => {
    e.preventDefault()
    let newCreature= {
      name,
      tag,
      description
    }

    const creature = await dispatch(createCreature(newCreature)).catch(err => setErrors(err.errors))

    if (creature) {
      let creaturePics = {
        url: url,
        creature_id: creature.id
      }

      await dispatch(createImage(creaturePics))
      //  await fetch('/api/images', {
      //     method: "POST",
      //     headers: {
      //       'Content-Type' : 'application/json'
      //     },
      //     body: JSON.stringify(creaturePics),
      // });
      // if (res.ok) {
          // await res.json();
          // console.log(res.json())
      // }
      history.push(`/creatures/${creature.id}`)
    }
  }


  return (
    <div className='usermenu__container'>
      <div className='usermenu__option'>
        <div className='usermenu__option' onClick={() => setDisplayCreate(true)}>Create Custom</div>
        <Popup open={displayCreate} onClose={()=> setDisplayCreate(false)}>
          <form className='create__form' onSubmit={handleCreate}>
            <div className='create__errors'>
              {errors.map((error) => (
                <div key={error} className='error__message'>{error}</div>
              ))}
            </div>
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
            <div className='form__item'>
              <input
                type="file"
                accept="image/*"
                onChange={upload}
              />
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
