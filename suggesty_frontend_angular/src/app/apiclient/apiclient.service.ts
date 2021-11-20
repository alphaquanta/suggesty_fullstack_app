import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { trackItem } from '../searchbox/searchbox.component';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { catchError, throwError } from 'rxjs';


export interface getPlaylistResponse {
  "RESULT"?:string
  "MESSAGE"?:string
  data?:trackItem[]
} 

const baseURL = environment.baseURL

@Injectable({
  providedIn: 'root'
})
export class APIClientService {

  constructor(private http: HttpClient) { }

  getPlaylist(genre:string):Observable<getPlaylistResponse>
  {
    return this.http.get<getPlaylistResponse>(baseURL+"/v1/tracks/"+genre);
  }

}

