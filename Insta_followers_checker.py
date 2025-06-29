import json
import streamlit as st
import zipfile

# Main checker
def upload_files(a,b):
    followers = json.load(a)  
    following = json.load(b)


    follower_id = []
    following_id = []
    for i in followers:
        inside = i.get('string_list_data', [])
        for l in inside:
            follower_id.append(l.get('value',''))
            

    vaues = following.get('relationships_following', [])
    for m in vaues:
        data = m.get('string_list_data', [])
        for z in data:
            following_id.append(z.get('value', ''))
    people = []
    for i in following_id:
        if i not in follower_id:
            people.append(i)
    
    

    
    if len(people) == 0:
        st.markdown("**All the people you follow are following you back!**")
    else:
        st.markdown(f"**There are total {len(people)} accounts which doesn't follow you back.**")
        st.markdown(f"**Accounts are:**")
        for k in people:
            st.text(f"- {k}")
    
    


# Streamlit app setup
col1,col2 = st.columns([1,8])
with col1:
    st.image('Instagram-Logo.png', width=70)
with col2:
    st.title("Insta Followback Checker")
st.header("Welcome.... 🚀") 
st.subheader("This app checks who doesn't follow you back!!!!")
st.text("Please upload the Zipped file or JSON files ('followers_1 & following') which you \nhave downloaded from Instagram.")

followers_file =''
following_file = ''
folders = st.file_uploader("Choose files", accept_multiple_files=True, type=["json", "zip"])
folder = None
for file in folders:
    if file.name == "followers_1.json":
        followers_file = file
    elif file.name == "following.json":
        following_file = file
    elif file.name.endswith(".zip"):
        folder = file
    else:
        st.warning("Please upload 'Zip' file folder or files named 'followers_1.json' and 'following.json' after unzipping the zipped file.")


# Check if both files are uploaded
if folder or (followers_file and following_file):
    if st.button("Check"):
        if followers_file and following_file:
            upload_files(followers_file, following_file)
        elif folder:
            with zipfile.ZipFile(folder, 'r') as z:
                
                followers_path = "connections/followers_and_following/followers_1.json"
                following_path = "connections/followers_and_following/following.json"

                # Check if the files exist
                if followers_path in z.namelist():
                    followers_file = z.open(followers_path)

                if following_path in z.namelist():
                    following_file = z.open(following_path)

                else:
                    st.warning("Required files not found in the ZIP. Please select correct zip file.")
                    exit()
            upload_files(followers_file, following_file)
        
        else:
            st.warning("Please upload both files before checking!")





# Instructions for the user
with st.expander("Please follow these steps, to use this app:"):

    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown("1. Open Instagram and login with your details.")
        st.markdown("2. Go to your profile and click on '**Settings**'.")
        st.markdown("3. Go to your '**See more in Account Center**' in Account Center.")
        st.markdown("4. Click on '**Your Information and permissions**' Under 'Account settings'.")
        st.markdown("5. Click on '**Download your information**'.")
        st.markdown("6. Go to '**Download or transfer information**' and select your instagram account.")
        st.markdown("7. Go to '**Some of your information**'.")
        st.markdown("8. Select '**Followers and following**' under '**Connections**' and hit '**Next**'.")
        st.markdown("9. Then Click on '**Download to this Device**'.")
        st.markdown("10. Format should be JSON and Date range should be '**All time**'.")
        st.markdown("11. Click on '**Create File**'.")
    st.markdown("**Note: This data will be sent to you over mail. Download it and upload zipped file or files by name 'followers_1' & 'following' after extracting the file.**")

