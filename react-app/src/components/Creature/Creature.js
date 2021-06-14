import React, {useState, useEffect} from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import './Creature.css'
import Navigation from '../Naviagtion/Navigation';
import Popup from 'reactjs-popup';
import {editCreature, getCreatures} from '../../store/creature'

const Creature = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [displayCreate, setDisplayCreate] = useState(false)
  const [name, setName] = useState('')
  const [tag, setTag] = useState('')
  const [description, setDescription]= useState('')
  const [errors, setErrors] = useState([]);
  const id = useParams()

  const allCreatures = useSelector(state => state.creature)
  // console.log('ALL CREATURES',allCreatures)
  const { creatureId } = useParams();
  // console.log(allCreatures[0].name)
  let creature = {};
  let creatureArr = [];
  for (const creat in allCreatures) {
    // console.log("CREAT", allCreatures[creat].id)
    if (allCreatures[creat].id === parseInt(creatureId)){
      creature = {...allCreatures[creat]}

   }
   creatureArr.push(allCreatures[creat].name)
  }
  // console.log('CREATURES ARRAY ------>', creatureArr)
  const allTags = useSelector(state => state.tag)
  // console.log('ALL TAGS', allTags)
  let cTag = {};
  for (const t in allTags) {
    // console.log("T------->", allTags[t].type)
    // console.log('CREATURE', creature)
    if (allTags[t].id === creature.tag_id){
      cTag = {...allTags[t]}
    }
  }
  // console.log('TAG----->', tag)
  // console.log(creature)
  // console.log(creature)
  // const dispatch = useDispatch()
  // allCreatures.forEach(creat => {
  //   if (creature.id === creatureId){
  //      creature = creat
  //   }
  // });
  // const creatures = useSelector(state => state.creature)
  // console.log("CREATURES", creatures)
  // const idx = Object.values(allCreatures)[]
  // console.log("KEYS??????", idx)
  const handleCreate = async (e) => {
    e.preventDefault()
    // console.log('CREATURES==========>', creatureArr)
    const idx = creatureArr.indexOf(creature.name)
    // console.log('IDX------>', idx)
    let newCreature= {
      id: creature.id,
      name,
      tag,
      description,
      idx
    }
    const editedCreature = await dispatch(editCreature(newCreature)).catch(err => setErrors(err.errors))
    // console.log('CREATURE ------->', creature)
    if (editedCreature) {
      history.push(`/creatures/${creature.id}`)
      await dispatch(getCreatures())
      setDisplayCreate(false)
    }
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
          <div className='edit__creature'
                onClick={() => setDisplayCreate(true)}
          >Edit</div>
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
              defaultValue={creature.name}
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
              defaultValue={creature.description}
              onChange={(e) => setDescription(e.target.value)}></textarea>
            </div>

            <button className='submit__create--edit'>Edit Creature</button>
          </form>
        </Popup>
          {creature.description}
        </div>
      </div>
    </div>
    )
}

export default Creature;
