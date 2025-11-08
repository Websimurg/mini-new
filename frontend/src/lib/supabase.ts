import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// Helper functions for common operations
export const supabaseHelpers = {
  // User authentication
  async signUp(email: string, password: string) {
    return await supabase.auth.signUp({
      email,
      password,
    })
  },

  async signIn(email: string, password: string) {
    return await supabase.auth.signInWithPassword({
      email,
      password,
    })
  },

  async signOut() {
    return await supabase.auth.signOut()
  },

  async getCurrentUser() {
    const { data: { user } } = await supabase.auth.getUser()
    return user
  },

  // Pinterest accounts
  async getPinterestAccounts(userId: string) {
    return await supabase
      .from('pinterest_accounts')
      .select('*')
      .eq('user_id', userId)
  },

  async createPinterestAccount(data: any) {
    return await supabase
      .from('pinterest_accounts')
      .insert(data)
  },

  // Pins
  async getPins(userId: string) {
    return await supabase
      .from('pins')
      .select('*')
      .eq('user_id', userId)
      .order('created_at', { ascending: false })
  },

  async createPin(data: any) {
    return await supabase
      .from('pins')
      .insert(data)
  },

  // Scheduled pins
  async getScheduledPins(userId: string) {
    return await supabase
      .from('scheduled_pins')
      .select(`
        *,
        pin:pins(*)
      `)
      .eq('pins.user_id', userId)
      .order('scheduled_for', { ascending: true })
  },

  // Analytics
  async getAnalytics(accountId: string, startDate: string, endDate: string) {
    return await supabase
      .from('analytics')
      .select('*')
      .eq('pinterest_account_id', accountId)
      .gte('date', startDate)
      .lte('date', endDate)
      .order('date', { ascending: false })
  },
}
