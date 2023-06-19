import streamlit as st

def project_summary():
    st.write("### Project Summary")

    # information from README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset contains house sale prices in Ames, Iowa,"
        f" There are a total of 23 property features which could influence the sale price of a house.\n"
        f" These features contain: first floor area, basement area, ground floor living area, overall quality"
        f", kitchen quality and second floor area etc.\n\n")
        
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.\n"
        f"* 2 - The client is interested to predict the house sale prices from her 4 inherited houses,"
        )
    
        # link to the project README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/pieterkdevilliers/pp5-heritage-housing)")
        