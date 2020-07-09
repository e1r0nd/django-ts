import React from "react";

type LiProps = {
  text: string;
};

/**
 * Render `<li>` element
 * @param {string} text Text to render
 */
export const Li = ({ text }: LiProps) => <li className="App-link">{text}</li>;
