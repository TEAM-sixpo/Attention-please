import styled, { css } from 'styled-components';
import { darken } from 'polished';
import palette from '../../lib/styles/palette';

const StyledButton = styled.button`
  width:92%;
  outline:none;
  border: 1px solid #fff;
  padding: 12px 20px;
  margin: 10px;
  border-radius: 20px;
  background: linear-gradient(to right, ${palette.PRIMARY}, ${palette.SUB}) !important;
    &:hover {
      background: linear-gradient(
        to right,
        ${darken(0.1, palette.PRIMARY)},
        ${darken(0.1, palette.SUB)}
      ) !important;
    }
  ${(props) =>
    props.maincolor &&
    css`
      background: linear-gradient(to right, ${palette.PRIMARY}, ${palette.SUB}) !important;
      &:hover {
        background: linear-gradient(
          to right,
          ${darken(0.1, palette.PRIMARY)},
          ${darken(0.1, palette.SUB)}
        )
      }
    `}
`;

const Button = props => <StyledButton {...props} />;

export default Button;