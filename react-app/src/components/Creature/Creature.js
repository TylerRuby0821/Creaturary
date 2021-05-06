import React, {useEffect, useState} from 'react';
import { Redirect, NavLink, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import './Creature.css'
import Navigation from '../Naviagtion/Navigation';
import { getCreature } from '../../store/creature';


const Creature = (creature) => {

  const { creatureId } = useParams();
  const dispatch = useDispatch()
  const [currCreature, setcurrCreature] = useState({})
  // const creatures = useSelector(state => state.creature)
  // console.log("CREATURES", creatures)
  useEffect(() => {
    (async () => {
        const creat = await dispatch(getCreature(creatureId))
        setcurrCreature(creat)
    })()

  }, [creatureId, dispatch])

  return (
    <div>
      <Navigation />
      {/* Thumbnail */}
      <div className='main__body--creature'>
        <span className='creature__name'>{currCreature.name}</span>
        <span className='creature__tag'>{currCreature.tag_id}</span>
        <div className='creature__decription'>{currCreature.description}</div>
      </div>
    </div>
    )
}

export default Creature;
