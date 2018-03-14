class QuestionsController < ApplicationController
    def new
    end

    def index
        @questions = Question.all
    end


    def create
        @question = Question.new(question_params)
        @question.save
        redirect_to @question
    end

    def show
        @question = Question.where(params[:title])
    end


    private

    def question_params
        params.require(:question).permit(:title, :text)
    end

end
