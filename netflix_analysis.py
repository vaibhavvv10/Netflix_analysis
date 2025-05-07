import pandas as pd

import plotly.express as <span class="cm-variable">px

import plotly.graph_objects as go

import plotly.io as pio

pio.templates.default</span> = "plotly_white"



netflix_data = pd.read_csv("/content/netflix_content_2023.csv")



netflix_data.head()

netflix_data['Hours Viewed'] = netflix_data['Hours Viewed'].replace(',', ''</span>, regex=True).astype(float)

netflix_data[['Title', 'Hours Viewed']].head()

# aggregate viewership hours by content type

content_type_viewership = netflix_data.groupby('Content Type')['Hours Viewed'].sum()

    go.Bar(

        x=content_type_viewership.index,

        y=</span>content_type_viewership.values,

        marker_color=['skyblue', 'salmon']

    )

])

fig.update_layout(

    xaxis_title='Content Type',

    yaxis_title='Total Hours Viewed (in billions)',

    xaxis_tickangle=0,

    height=500,

    width=800

)

# aggregate viewership hours by language

language_viewership = netflix_data.groupby('Language Indicator')['Hours Viewed'].sum().sort_values(ascending=False)

fig = go.Figure(data=[

        x=language_viewership.index,

        y=language_viewership.values,

        marker_color='lightcoral'

])</span>

    title='Total Viewership Hours by Language (2023)',

    xaxis_title='Language',

    yaxis_title='Total Hours Viewed (in billions)',

    xaxis_tickangle=45,

    height=600,

    width=1000

fig.show()

# convert the "Release Date" to a datetime format and extract the month

netflix_data['Release Date'] = pd.to_datetime(netflix_data['Release Date'])

netflix_data['Release Month'] = netflix_data['Release Date'].dt.month

=E2=80=8B

# aggregate viewership hours by release month

monthly_viewership = netflix_data.groupby('Release Month')['Hours Viewed'].sum()

fig = go.Figure(data=[

    go.Scatter(

        x=monthly_viewership.index,

        y=monthly_viewership.values,

        mode='lines+markers',

        marker=dict(color='blue'),

        line=dict(color='blue')

fig.update_layout(

    title='Total Viewership Hours by Release Month (2023)',

    xaxis_title='Month',

    yaxis_title='Total Hours Viewed (in billions)',

    xaxis=dict(

        tickmode='array',

        tickvals=list(range(1, 13)),

        ticktext=</span>['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', <span class="cm-string">'Dec']

    ),

# extract the top 5 titles based on viewership hours

top_5_titles = netflix_data.nlargest(5, 'Hours Viewed')



# aggregate viewership hours by content type and release month

monthly_viewership_by_type = netflix_data.pivot_table(index='Release Month',

                                                      columns='Content Type',

                                                      values='Hours Viewed',

                                                      aggfunc='sum')

fig = go.Figure()

for content_type in monthly_viewership_by_type.columns:

    fig.add_trace(

        go.Scatter(

            x=monthly_viewership_by_type.index,

            y=monthly_viewership_by_type[content_type],</span>

            name=</span>content_type

        )

    title='Viewership Trends by Content Type and Release Month (2023)',

    yaxis_title='Total Hours Viewed (in billions)',

    xaxis=dict(

        tickmode='array',

        tickvals=list(range(1, 13)),

        ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    <span class="cm-variable">height=600,

    width=1000,

    legend_title='Content Type'

fig.show()

# define seasons based on release months

def get_season(month):

    <span class="cm-keyword">if month in [12, 1, 2]:</span>

    elif month in [3, 4, 5]:

        return 'Spring'

    elif month in [6, 7, 8]:

        return 'Summer'

    else:

        return 'Fall'

=E2=80=8B

# apply the season categorization to the dataset

netflix_data['Release Season'] = netflix_data['Release Month'].apply(get_season)

# aggregate viewership hours by release season

seasonal_viewership = netflix_data.groupby('Release Season')['Hours Viewed'].sum()

    go.Bar(

        x=seasonal_viewership.index,

        y=seasonal_viewership.values,

        marker_color='orange'

    title='Total Viewership Hours by Release Season (2023)',

    xaxis_title='Season',

    yaxis_title='Total Hours Viewed (in billions)',

    xaxis_tickangle=0,</pre>

    width=800,

        categoryorder=</span>'array',

        categoryarray=seasons_order

monthly_releases = netflix_data['Release Month'].value_counts().sort_index()

monthly_viewership = netflix_data.groupby('Release Month')['Hours Viewed'].sum()

fig.add_trace(

        x=monthly_releases.index,

        y=monthly_releases.values,

        name='Number of Releases',

        <span class="cm-variable">opacity=0.7,

        yaxis='y1'

)</pre>

</pre>

fig.add_trace(

        x=monthly_viewership.index,

        y=monthly_viewership.values,

        name='Viewership Hours',

        mode=</span>'lines+markers',

        marker=dict(color=<span class="cm-string">'red'),

        line=dict(color='red'),

        yaxis='y2'

    )

    title='Monthly Release Patterns and Viewership Hours (2023)',

        title='Month',

        tickvals=list(range(1, 13)),

        ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', <span class="cm-string">'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    yaxis=dict(

        title='Number of Releases',

        showgrid</span>=False,

        side='left'

        title='Total Hours Viewed (in billions)',

        overlaying='y',

        showgrid=False

    ),

    legend=dict(

        x=1.05,  

        y=1,

        orientation='v',

        xanchor='left'</span>

fig.show()

netflix_data['Release Day'] = netflix_data['Release Date'].dt.day_name()

<span cm-text="">

weekday_releases = netflix_data['Release Day'].value_counts().reindex(

    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# aggregate viewership hours by day of the week

weekday_viewership = netflix_data.groupby('Release Day')['Hours Viewed'].sum().reindex(

    go.Bar(

        x=weekday_releases.index,

        y=weekday_releases.values,</pre>

        name='Number of Releases',

        marker_color='blue',

        opacity=0.6,

        yaxis='y1'

        x=weekday_viewership.index,

        y=weekday_viewership.values,

        mode='lines+markers',

        marker=dict(color='red'),

        line<span class="cm-operator">=dict(color='red'),

fig.<span class="cm-property">update_layout(

    title='Weekly Release Patterns and Viewership Hours (2023)',

    xaxis=</span>dict(

        title='Day of the Week',

        categoryarray=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        showgrid=False,

    yaxis2=</span>dict(

        title='Total Hours Viewed (in billions)',

        side='right',

    legend=dict(

        y<span class="cm-operator">=1,

    ),

# define significant holidays and events in 2023

important_dates = [

    '2023-01-01',  <span class="cm-comment"># new year's day

    '2023-02-14',  # valentine's ay

    '2023-07-04',  # independence day (US)

    '2023-10-31',  # halloween

    '2023-12-25'   # christmas day

]

# convert to datetime

important_dates = pd.to_datetime(important_dates)

# check for content releases close to these significant holidays (within a 3-day window)

holiday_releases = netflix_data[netflix_data['Release Date'].apply(

    lambda x: any((x - date).days in range(-3, 4) for date in important_dates)

)]

# aggregate viewership hours for releases near significant holidays

holiday_viewership = holiday_releases.groupby('Release Date')['Hours Viewed'].sum()

holiday_releases[['Title', 'Release Date', 'Hours Viewed']]