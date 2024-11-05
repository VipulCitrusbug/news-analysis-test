# News Analysis using LLM and News API

This project provides a simple API using FastAPI to fetch news articles based on keywords and analyze them using a Large Language Model (LLM) from OpenAI.

## Installation

1. Create a virtual environment and activate it.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set the environment variables `NEWSAPI_API_KEY`, `DEFAULT_OPENAI_MODEL`, and `OPENAI_API_KEY` with your API keys.
4. Run the application using `uvicorn app.main:app --reload`.
5. Open the swagger UI at http://localhost:8000/docs to view the API endpoints.

## API Endpoints

### 1. Get News Articles

==> GET /news/analyze/

- Fetches news articles based on the provided keywords and analyzes them using the LLM.

**Parameters:**

- keywords: Keywords to search for news. (use comma (,) to separate multiple keywords)

**Example:**
`GET /news/analyze/?keywords=apple,google`

**Response:**

```
{
  "data": {
    "title": "The Uncertainty Is the Hardest Part",
    "summary": "The article discusses the pervasive uncertainty experienced by individuals, particularly in the context of the upcoming presidential election. It highlights how this uncertainty leads to anxiety and mental unrest, emphasizing that while people can make choices, the outcomes remain unpredictable. The author suggests a need for individuals to accept and explore uncertainty, underscoring the importance of human connection in coping with it, especially in politically polarized times.",
    "key_points": [
      "Uncertainty is a significant source of anxiety and mental disturbance for individuals.",
      "The unpredictability of the future is compounded by the current political climate, particularly regarding the presidential election.",
      "Therapists are seeing an increased focus on electoral concerns in their sessions, reflecting widespread anxiety.",
      "The acceptance of uncertainty is crucial for mental well-being and decision-making.",
      "The state of societal polarization exacerbates feelings of uncertainty and fear among different political groups.",
      "A call for recognizing our limitations and the importance of community support in uncertain times."
    ],
    "sentiment_analysis": -0.5,
    "topic": "Mental Health",
    "content": "If theres anything that keeps me and my psychotherapist colleagues in business, its uncertainty. You can dance on the horns of a dilemma for only so long before obsession, anxiety, depression -- the staples of mental unease -- set in. The need to resolve uncertainty feels urgent and only sharpens the suffering of not knowing. As much as we might like, and no matter how hard we try, we cannot know the future -- about an election or anything else. This feels cruel, not only because life continually presents us with ambiguity, but also because our brain is a prediction machine. As the philosopher Andy Clark puts it, the mind is a kind of constantly running simulation of the world around us -- or at least, the world as it matters to us. We have a mental model of how the world works, and we update it as we get new information. When new information is ambiguous, we get confused, and if the confusion cannot resolve, we suffer. Live with someone who treated you well yesterday and abusively today, your ability to predict is diminished, and with it the confidence to make a choice. Next stop, my office, where you are sure to hear that you have to learn not only to tolerate the uncertainty of making a decision, but also to welcome it, to explore and elucidate it, so that you can carry that knowledge into the future. Which is all well and fine if the uncertainty is about whether to leave a marriage or get into one, or what to do when someone you love is hurting you, or any of the other matters that bring people in to see me. While my clients havent stopped having those dilemmas, their uncertainty these days focuses on a matter about which they can decide all they want -- and they will, when they vote -- but they will remain uncertain about the outcome. I dont think a single therapy hour has passed in the past month without at least a mention of the presidential election, and not as a pleasantry, like a comment on the weather, but as a source of sleeplessness or jitters or some other kind of psychic suffering. Their future is unknown, and the data with which to update their models -- polls and pundits and talks with their neighbors -- only reinforces the uncertainty. I dont poll my clients for their political leanings, but if I had to guess, Id say they skew Harris, or at least not-Trump. But everyone, including the Trumpers, seems equally unsure about what will happen and plagued by not knowing. Their fears, as befits our thoroughly polarized times, are mirror images of each other millions of people rounded up, interned and deported millions of people swarming over the southern border to rape and pillage. Because one of these worries is more based in fact than the other, I support the fears and outrage of the Harrisers, while trying, as sympathetically as possible, to suggest that the Trump supporters check their facts, or even reminding them of the awful legacy that has come from politicians who speak of targeting the enemy from within. But I dont know the future either, so not only am I uncertain of what will happen after Election Day although I have my guesses, and they are not pleasant, Im not sure what will become of these conversations. I take them to be symptomatic of developments that, like most important aspects of life, are impossible to predict but possible to understand in retrospect. In this case, the unraveling of a social fabric that once felt as certain and present as the air, but now, when we cant even agree on how to manage a pandemic or what constitutes fascism, seems as fragile as an old, worn-out linen. In the unraveling, I find myself offering counsel that I offered before only in the face of hopeless circumstance -- a terminal illness, say, or the death of a loved one that many of the most important parts of our lives are beyond our control, and equanimity cannot be had without surrender to circumstance. This is one thing of which we can be certain Historys wheel is indifferent, not unlike cancer or a cheating spouse, and can crush us willy-nilly. Which means, I hear myself saying to my own surprise and dismay, that it falls upon us to cultivate helplessness. Thats not to say we should cultivate inaction or nihilism. Its to say that we really have no choice but to recognize just how tiny we are, and how much we therefore need one another, and in uncertain times even more. Our minds, as glorious as they are, cannot tell us the future, nor save us from it. The uncertainty we live in right now is only a reminder that this is our lot. Tempting as it might be, it would be far worse to give ourselves over to a man who is never uncertain, even when he is wrong. And should he succeed in huckstering enough of us into doing that, then it will fall to the rest of us to join together to protect the beautiful uncertainties of democracy.",
    "published_date": "2024-11-05T10:36:29Z"
  },
  "message": "Success"
}
```
