import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch} from "react-router-dom";
import { useDispatch} from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import { authenticate } from "./store/session";
import LandingPage from './components/LandingPage/LandingPage'
import MainPage from './components/MainPage/MainPage'
import Creature from "./components/Creature/Creature";
import {getCreatures} from './store/creature'
import {getTags} from './store/tag'
import SearchLore from './components/Search/SearchLore'
import SearchAz from './components/Search/SearchAz'
import SearchCustom from './components/Search/SearchCustom'
import Search from './components/Search/Search'

function App() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);
  const [creatures, setCreatures] = useState({})
  const [tags, setTags] = useState({})

  useEffect(() => {
    dispatch(getCreatures())
  }, [creatures, dispatch])

  useEffect(() => {
    dispatch(getTags())
  }, [tags, dispatch])

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }


  return (
    <BrowserRouter>
      {/* <NavBar setAuthenticated={setAuthenticated} /> */}
      <Switch>
        <Route path="/" exact={true}>
          <LandingPage />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/creatures" exact={true}>
          <MainPage />
        </Route>
        <Route path="/creatures/lore" exact={true}>
          <SearchLore />
        </Route>
        <Route path="/creatures/custom" exact={true}>
          <SearchCustom />
        </Route>
        <Route path="/creatures/a-z" exact={true}>
          <SearchAz />
        </Route>
        <Route path="/creatures/search" exact={true}>
          <Search />
        </Route>
        <Route path="/creatures/:creatureId" exact={true}>
          <Creature />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
