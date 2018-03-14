class RemoveUsersEmail < ActiveRecord::Migration[5.1]
  def self.up
  	remove_column :users, :email
  end
end
