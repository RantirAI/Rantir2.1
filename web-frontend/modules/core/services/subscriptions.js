export default (client) => {
    return {
      getUserGroups() {
        return client.get('/subscription/user-groups')
      },
      createNewUserGroup(values) {
        return client.post('/subscription/create-user-group/', values)
      },
      createNewPlan(values) {
        return client.patch('/settings/update/', values)
      },
      getPlans(){
        return client.get('/subscription/plans/')
      },
      getDatabases(){
        return client.get('/commerce/databases')
      },
      getPlans(){
        return client.get('/commerce/plans')
      },
      getSubscriptionOverview(){
        return client.get('commerce/subscriptions/overview')
      }
    }
  }