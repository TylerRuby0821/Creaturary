import React, {useState} from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import './Creature.css'
import Navigation from '../Naviagtion/Navigation';
import Popup from 'reactjs-popup';
import {editCreature, getCreatures} from '../../store/creature'
import { addFavorite, removeFavorite } from '../../store/favorite';

const Creature = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [displayCreate, setDisplayCreate] = useState(false)
  const [errors, setErrors] = useState([]);
  const allCreatures = useSelector(state => state.creature)
  const { creatureId } = useParams();
  const images = useSelector(state => state.image)
  const favorites = useSelector(state => state.favorite)
  const imageArr = []
  //Creature Array
  let creature = {};
  let creatureArr = [];
  for (const creat in allCreatures) {
    if (allCreatures[creat].id === parseInt(creatureId)){
      creature = {...allCreatures[creat]}
    }
    creatureArr.push(allCreatures[creat].name)
  }
  //Tags assignment
  const allTags = useSelector(state => state.tag)
  let cTag = {};
  for (const t in allTags) {
    if (allTags[t].id === creature.tag_id){
      cTag = {...allTags[t]}
    }
  }

  let favArr = []
  for (const fav in favorites) {
     favArr.push(favorites[fav])
  }

  //Image assignment
  for (const image in images) {
    if (images[image].creature_id === Number(creatureId))
    imageArr.push(images[image])
  }

  const [name = creature.name, setName] = useState(creature.name)
  const [tag = creature.tag, setTag] = useState(creature.tag)
  const [description = creature.description, setDescription]= useState(creature.description)

  const handleCreate = async (e) => {
    e.preventDefault()
    const idx = creatureArr.indexOf(creature.name)
    let newCreature= {
      id: creature.id,
      name,
      tag,
      description,
      idx
    }
    const editedCreature = await dispatch(editCreature(newCreature)).catch(err => setErrors(err.errors))
    if (editedCreature) {
      history.push(`/creatures/${creature.id}`)
      await dispatch(getCreatures())
      setDisplayCreate(false)
    }
  }
  const isItThere = favArr.filter(e=> e.id === creature.id)
  const [favorited, setFavorited] = useState(isItThere.length > 0)

  const handleFavorite = async (e) => {
    e.preventDefault()
    let favorite = {
      creature_id: creature.id
    }
    await dispatch(addFavorite(favorite))
    setFavorited(favorited)
  }

  const handleUnfavorite = (e) => {
    e.preventDefault()
    dispatch(removeFavorite(creature))
    setFavorited(favorited)
  }

  return (
    <div>
      <Navigation />
      {/* Thumbnail */}
      <div className='main__body--creature'>
        <span className='creature__name'>{creature.name}</span>
        {cTag.type === 'Custom' ? <span className='creature__tag--Custom'>{cTag.type}</span> : <span className='creature__tag--Lore'>{cTag.type}</span> }
        {/* <span className='creature__tag'>{tag.type}</span> */}
        <div className='creature__decription'>
        <div className='top__bar'>
          {favorited ?
          <div className='favorite__icon' onClick={handleUnfavorite}>
                    <i className="fas fa-heart"></i>
          </div>
          :
          <div className='favorite__icon' onClick={handleFavorite}>
                    <i className="far fa-heart"></i>
          </div>
          }
            <div className='edit__creature'
                  onClick={() => setDisplayCreate(true)}
            >Edit</div>
        </div>
          <Popup
          open={displayCreate}
          onClose={()=> setDisplayCreate(false)}
          >
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
              value={name}
              onChange={(e) => setName(e.target.value)}></input>
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
              defaultValue={description}
              onChange={(e) => setDescription(e.target.value)}></textarea>
            </div>

            <button className='submit__create--edit'>Edit Creature</button>
          </form>
        </Popup>
        {imageArr.length >0 &&
          <div><img className='creature__picture' src={imageArr[0].url} alt='Nothing to show yet.'></img></div>
        }
          {creature.description}
        </div>
      </div>
    </div>
    )
  }

export default Creature;
