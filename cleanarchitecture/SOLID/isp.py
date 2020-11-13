


# Interface Segregation Principle


# Codes should not be forced to depend on methods they do not use.
 # Classes should not have access to behavior they do not use.


# Implementation

# class Blog:

#     def edit_post(self):
#         print("Post edited.")

#     def delete_post(self):
#         print("Post removed.")

#     def create_post(self):
#         print("Post created")
        

# class Moderator(Blog):

#     pass



# moderator = Moderator()
# moderator.edit_post()
# moderator.delete_post() #moderator should not have privilage to delete a post.


# ISP favours -> Composition Over Inheritance

# Using ISP


class Blog:

    def edit_post(self):
        print("Post edited.")

    def delete_post(self):
        print("Post removed.")

    def create_post(self):
        print("Post created")




class CanEdit:

    def edit_post(self):
        print('Post Edited.')

class Moderator(CanEdit):

    pass

moderator = Moderator()
moderator.edit_post()

