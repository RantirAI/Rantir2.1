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
        return {
          data: [
            { id: 1, name: 'Drivers' },
            { id: 2, name: 'Customers' },
            { id: 3, name: 'Orders' }
          ]
        };
        return client.get('/commerce/databases')
      },
      getPlans(){
        return {
            data: [
              { id: 1, name: 'Free Plan' },
              { id: 2, name: 'Premium' },
              { id: 3, name: 'Basic' }
            ]
        };
        return client.get('/commerce/plans')
      },
      getSubscriptionOverview(){
        return {
          data : {
            "total_members": 2300,
            "signups_last_month": 24,
            "paid_members": 324,
            "monthly_revenue": 12450,
          }
        }
        return client.get('commerce/subscriptions/overview')
      }
    }
  }