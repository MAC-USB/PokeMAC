class AddAnswersUsers < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :answers, :int
  end
end
