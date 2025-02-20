import subscriptionsService from '@baserow/modules/core/services/subscriptions'

export const state = () => ({
    loaded: false,
    plans: [],
    userGroups: [],
    userGroup: {},
    databaselist: [],
    settings: {},
    subscriptionOverview: null,
})

export const mutations = {
  UPDATE_PLAN_LIST(state, values) {
    state.settings = values
  },
  UPDATE_USER_GROUPS(state, values) {
    state.userGroups = Object.assign({}, state.userGroups, values)
  },
  SET_LOADED(state, value) {
    state.loaded = value
  },
  SET_SUBSCRIPTION_OVERVIEW(state, value) {
    state.subscriptionOverview = value
  },
  SET_DATABASE_LIST(){
    
  }
}

export const actions = {
  async getUserGroups({ commit }) {
    const { data } = await subscriptionsService(this.$client).getUserGroups()
    commit('UPDATE_USER_GROUPS', data)
    commit('SET_LOADED', true)
  },
  async getPlans({ commit, getters }, values) {
    const { data } = await subscriptionsService(this.$client).getPlans()
    commit('UPDATE_PLAN_LIST', values)
  },
  async createNewUserGroup({ commit }, values) {
    const { data } = await subscriptionsService(this.$client).createNewUserGroup(values)
    commit('UPDATE_USER_GROUPS', data)
  },
  async getSubscriptionOverview({ commit }) {
    const { data } = await subscriptionsService(this.$client).getSubscriptionOverview()
    commit('SET_SUBSCRIPTION_OVERVIEW', data)
  },
  async getSubscriptionOverview({ commit }) {
    const { data } = await subscriptionsService(this.$client).getDatabases()
    commit('SET_SUBSCRIPTION_OVERVIEW', data)
  },
  async getDatabaseList({ commit }) {
    
  },
  async getSettings({ commit }) {
  },
}

export const getters = {
  isLoaded(state) {
    return state.loaded
  },
  plans(state) {
    return state.plans
  },
  subscriotionOverview(state) {
    return state.subscriptionOverview
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
